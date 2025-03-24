p1 >> pluck(dur=4, oct=3, lpf=500)

n1 >> noise(4, lpf=1300, hpf=1300, blur=4, dur=4, amp=1)

p1 >> pluck(
    [0, 1, 4, (12, 14)],
    dur=[rest(1)] + [1] * 3,
    oct=3,
    amp=1,
    lpf=500,
)

v1 >> viola(
    [-1, 0, 1/2, 1, 2, 1, -99, 1/2, 1, 2, 3.5, 5, 4, -99],
    dur=(([1/2] * 6 + [rest(1)])*2),
    blur=2,
    amp=1,
    vib=8,
    lpf=800,
    drive=1,
    chop=1,
    pshift=PRand(3),
).every(1, "stutter", 4)
q1 >> play("       ( z)", sample=1, amp=3)

Clock.bpm = 160

q2 >> play("x(*[**])", amp=2)
q1 >> play("       ( [!...])", amp=4, sample=2)

u1 >> bass(0, amp=2)

u3 >> pluck([0, 2, 4], amp=12, dur=PDur(3, 4))

u4 >> karp(0, amp=5, vib=0, slide=1, dur=1/4)
