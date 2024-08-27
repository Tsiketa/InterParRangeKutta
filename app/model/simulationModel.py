import numpy as np

class SimulationModel:
    def __init__(self, daily, initial):
        self.daily = daily
        self.initial= initial

    def trigonometrical_function(self, t, cost):
        amplitude = 10
        frequency = 2 * np.pi / 30
        return amplitude * np.sin(frequency * t) + self.daily

    def run_simulation(self, duration):
        t_values, values = self.runge_kutta_4(self.trigonometrical_function, 0, self.initial, 0.1, duration)
        return t_values, values

    def runge_kutta_4(self, f, t0, y0, h, tf):
        t_values = np.arange(t0, tf + h, h)
        y_values = np.zeros(len(t_values))
        y_values[0] = y0

        for i in range(1, len(t_values)):
            t = t_values[i-1]
            y = y_values[i-1]
            k1 = h * f(t, y)
            k2 = h * f(t + 0.5*h, y + 0.5*k1)
            k3 = h * f(t + 0.5*h, y + 0.5*k2)
            k4 = h * f(t + h, y + k3)
            y_values[i] = y + (1/6) * (k1 + 2*k2 + 2*k3 + k4)

        return t_values, y_values
