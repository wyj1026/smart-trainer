# coding: utf-8

from ai.trainer import Trainer
from ai.preprocess import *
from ai.data.joint_coords import columns
from ai.suggestions import squat_suggestions

class RealTimeTrainer(Trainer):
    def __init__(self, targets, buffer_size={"squat": 20}):
        super(RealTimeTrainer, self).__init__(targets=targets)
        self.buffer_size = buffer_size
        self.buffer = {}
        for k in self.buffer_size.keys():
            self.buffer[k] = []

    def load_classifier(self, exercise_name, file_path):
        self.classifiers[exercise_name] = ai.load(file_path)

    def update_buffer(self, exercise, new_start_index):
        self.buffer[exercise] = self.buffer[exercise][new_start_index:]

    def update(self, exercise, realtime_data, accept_suggestions, processing=False, delta=10, ctn=1):
        if processing:
            self.process(realtime_data)
        self.buffer[exercise].extend(realtime_data)
        if len(self.buffer[exercise]) > self.buffer_size[exercise]:
            data_frame = data.convert_data_into_DF(self.buffer[exercise], columns)
            indexs = segmentation.get_min_coords(data_frame.get("SpineBaseY"), delta=delta, ctn=ctn)
            if len(indexs) >= 2:
                result = self.classify(exercise, self.buffer[exercise], delta=delta, ctn=ctn)
                self.update_buffer(exercise, indexs[-1]-6)
                if accept_suggestions:
                    return self.get_suggestions(result)
                else:
                    return result
        else:
            return None

    def process(self, frames):
        for frame in frames:
            for i in range(len(frame)):
                frame[i] = -1 * frame[i]
                if i%3 == 0:
                    frame[i] = frame[i]/100

    def get_suggestions(self, r):
        result = {}
        for i in range(len(self.targets)):
            result[self.targets[i]] = [repeat[i] for repeat in r]
        return squat_suggestions.get(result)

if __name__ == "__main__":
    path="./ai/classification/squat_classifiers.pk"
    targets = ["stance_shoulder_width", "knees_over_toes", "bend_hips_knees", "back_hip_angle", "depth"]
    #targets = ["stance_shoulder_width", "knees_over_toes"]
    ai = RealTimeTrainer(targets=targets)
    ai.load_classifier("squat", path)
    #print(ai.classifiers)
    test_data = data.read_data("./ai/data/squat_test/squatData2.txt")
    #test_data = data.read_data("./ai/data/raw_squat_data/squatData35.txt")
    for frame in test_data:
        r = ai.update("squat", [frame], accept_suggestions=True, processing=True, delta=10, ctn=1)
        #r = ai.update("squat", [frame], accept_suggestions=False, processing=False, delta=30, ctn=10)
        if r:
            print(r)
