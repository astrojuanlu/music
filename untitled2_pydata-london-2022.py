b1 >> bass(2, oct=4, fmod=0.2, amp=1.2, dur=4)
b3 >> growl(2, dur=[0.5, rest(3.5)])
b4 >> bass(2, dur=2, oct=(5,4), amp=0.75)
b1.stop()
b3.stop()
b4.stop()


d1 >> play("<x-x-><  *( [**])>")
d2 >> play("!", dur=8, sample=range(1, 5))
d1.stop()
d2.stop()

c1 >> charm(2, dur=[1, rest(3)])
c2 >> klank(2)
c1.stop()
c2.stop()

p1 >> pluck(var([(2, 4, 6), (2, 4, 7)], [12, 4]), dur=P[1, 3/4, 3/4, 1, 2/4], amp=1)

p1.solo(0)

Clock.bpm = 60
q1 >> pads([7, 1, 3.5, 1], dur=1/2).every(1/2, "stutter", 2)
def coda():
    dur = ([1] * 3 + [1.5, 0.5, 1]) * 2 + [1] * 3 + [9]
    h1 >> pads([4, 4, 5, 3.5, 4, 5, 6, 6, 7, 6, 5  , 4, 5, 4, 3.5, 4], dur=dur, vib=0, amp=2, room=10)
    h2 >> bass([4, 2, 0, 1, 2, 3.5, 4, 2, 0, 1, 1.5, 2, 0, 1, 1, 4], oct=5, dur=dur, amp=1, room=10)
    h_all.solo()
    Clock.future(int(Clock.mod(24) - Clock.now()) + 24, Clock.clear)
Clock.future(int(Clock.mod(24) - Clock.now()), coda)

# GOD SAVE PYDATA LONDON!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
