import nasco_controller
c = nasco_controller.controller()
beams = c.hemt.beam_list
print(beams)
[c.hemt.output_hemt_voltage(b, vd=0, vg1=0, vg2=0) for b in beams]
