from PIL import Image
from time import time

from Scene_files.All_features_Scene import *


if __name__ == "__main__":

	img = Image.new("RGB", (W,H))

	t1 = time()
	img = render_loop(scene, img)
	t2 = time()
	
	TotalTime_s = t2-t1
	TotalTime_m = Minutes(TotalTime_s)
	print(f"{TotalTime_s} \n {TotalTime_m}")

	file_name = f"Output/ {scene.f_name} {TotalTime_s}"
	out_frmt = "png"

	img.save(f"{file_name}.{out_frmt}")
