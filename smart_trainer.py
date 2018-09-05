# coding: utf-8

from ai.ai import Trainer
from ai.preprocess import *
from ai.data.joint_coords import columns
from ai.suggestions import squat_suggestions

class RealTimeTrainer(Trainer):
    def __init__(self, targets, buffer_size={"squat": 100}):
        super(RealTimeTrainer, self).__init__(targets=targets)
        self.buffer_size = buffer_size
        self.buffer = {}
        for k in self.buffer_size.keys():
            self.buffer[k] = []

    def load_classifier(self, exercise_name, file_path):
        self.classifiers[exercise_name] = ai.load(file_path)

    def update_buffer(self, exercise, new_start_index):
        self.buffer[exercise] = self.buffer[exercise][new_start_index:]

    def update(self, exercise, realtime_data, accept_suggestions):
        self.buffer[exercise].extend(realtime_data)
        if len(self.buffer[exercise]) > self.buffer_size[exercise]:
            data_frame = data.convert_data_into_DF(self.buffer[exercise], columns)
            indexs = segmentation.get_min_coords(data_frame.get("SpineBaseY"), delta=50)
            if len(indexs) >= 2:
                result = self.classify(exercise, self.buffer[exercise])
                self.update_buffer(exercise, indexs[-1]-10)
                if accept_suggestions:
                    return self.get_suggestions(result)
                else:
                    return result
        else:
            return None

    def get_suggestions(self, r):
        result = {}
        for i in range(len(self.targets)):
            result[self.targets[i]] = [repeat[i] for repeat in r]
        return squat_suggestions.get(result)

if __name__ == "__main__":
    path="./ai/classification/squat_classifiers.pk"
    targets = ["stance_shoulder_width", "knees_over_toes", "bend_hips_knees", "back_hip_angle", "depth"]
    ai = RealTimeTrainer(targets=targets)
    ai.load_classifier("squat", path)
    test_data = data.read_data("./ai/data/raw_squat_data/squatData19.txt")
    for frame in test_data:
        r = ai.update("squat", [frame], accept_suggestions=True)
        if r:
            print(r)
