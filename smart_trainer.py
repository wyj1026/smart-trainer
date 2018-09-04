# coding: utf-8

from ai.ai import Trainer
from ai.preprocess import *
from ai.data.joint_coords import columns


class RealTimeTrainer(Trainer):
    def __init__(self, buffer_size={"squat": 100}):
        super(RealTimeTrainer, self).__init__()
        self.buffer_size = buffer_size
        self.buffer = {}
        for k in self.buffer_size.keys():
            self.buffer[k] = []

    def load_classifier(self, exercise_name, file_path):
        self.classifiers[exercise_name] = ai.load(file_path)

    def update_buffer(self, exercise, new_start_index):
        self.buffer[exercise] = self.buffer[exercise][new_start_index:]

    def update(self, exercise, realtime_data, targets):
        self.buffer[exercise].extend(realtime_data)
        if len(self.buffer[exercise]) > self.buffer_size[exercise]:
            data_frame = data.convert_data_into_DF(self.buffer[exercise], columns)
            indexs = segmentation.get_min_coords(data_frame.get("SpineBaseY"), delta=50)
            if len(indexs) >= 2:
                result = self.classify(exercise, self.buffer[exercise], targets)
                self.update_buffer(exercise, indexs[-1]-10)
                return result
        else:
            return None


if __name__ == "__main__":
    path="./ai/classification/squat_classifiers.pk"
    ai = RealTimeTrainer()
    ai.load_classifier("squat", path)
    test_data = data.read_data("./ai/data/raw_squat_data/squatData14.txt")
    targets = ["stance_shoulder_width", "knees_over_toes", "bend_hips_knees", "back_hip_angle", "depth"]
    for frame in test_data:
        r = ai.update("squat", [frame], targets)
        if r:
            print(r)
