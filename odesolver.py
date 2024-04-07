import math

def euler_method(func, y0, t0, tn, h):
    t_values = [t0]
    y_values = [y0]

    while t_values[-1] < tn:
        t_next = t_values[-1] + h
        y_next = y_values[-1] + h * func(t_values[-1], y_values[-1])
        t_values.append(t_next)
        y_values.append(y_next)

    return t_values, y_values

def simple_oscillator(t, y):
    return math.sin(t) + math.cos(t)
initial_y = 0  
initial_t = 0  
final_t = 10   
step_size = 0.1  
t_values, y_values = euler_method(simple_oscillator, initial_y, initial_t, final_t, step_size)
print("t\t\t y(t)")
print("--------------------")
for t, y in zip(t_values, y_values):
    print(f"{t:.2f}\t\t {y:.6f}")
