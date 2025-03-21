bd >> play("x ", amp=2)

hh >> play(" [--]")

x1 >> play("(*[(DE)---])   ", sample=0)

b1 >> fuzz(amp=[1] + [0] * 3, tremolo=8)

o1 >> sinepad(0, vib=5)

b2 >> space([0] * 2 + [-7] * 2, amp=[2, 0] * 2)

o2 >> pluck([0, 1.5, 4, 1.5], dur=1/4)

o3 >> karp([(0, 1.5, 4)], dur=1/8, amp=0.75)

a1 >> pluck(0, dur=1, amp=0.25, vib=0, drive=0.5)

