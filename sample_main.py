from picture_lib.plmaths.plalgos.picrunch import Picrunch
from picture_lib.plimages.image_engine import GeneratorEngine

#picomp = Picrunch(10, 1048579, "output/pi_calcul.pi")

engine = GeneratorEngine(1024, 1024, "output/pi_calcul.pi")
engine.encode_binaries()
engine.set_output_dir("output")
engine.set_output_name_format("picture")
engine.run_one_shot_bw()

