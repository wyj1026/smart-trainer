# coding: utf-8

tips = {
   "stance_shoulder_width": "注意双脚与肩膀同宽度",
   "knees_over_toes": "注意膝盖不要超过脚尖",
   "bend_hips_knees": "请胯部和膝盖同时运动！",
   "back_hip_angle": "注意脊背前倾角度！",
   "depth": "注意下蹲深度！",
   "good": "做得很好，请保持"
}


def get(results, good_ratio=0.8, bad_ratio=0.2):
   suggestions = {}
   for key, labels in results.items():
      for label in set(labels):
         frequency = labels.count(label)
         ratio = frequency/len(labels)
         if label == 0 and ratio > good_ratio:
            suggestions[key] = tips["good"]
         elif label != 0 and ratio > bad_ratio:
            if key in suggestions:
               suggestions[key] += "\n" + tips[key]
            else:
               suggestions[key] = tips[key]
   return suggestions
