
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QFormLayout, QLineEdit, QPushButton, QLabel, QMainWindow, QStatusBar
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt

class SimulationView(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Simulation de Coût d'Intervention")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        # Grand titre centré
        self.title_label = QLabel("Simulation Par Range Kutta")
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setFont(QFont("Arial", 24, QFont.Bold))
        self.layout.addWidget(self.title_label)

        self.form_layout = QFormLayout()
        self.layout.addLayout(self.form_layout)

        # Champs de saisie avec style personnalisé
        self.duration_label = QLabel("Durée de l'intervention (jours)")
        self.duration_label.setFont(QFont("Times New Roman", 12))
        self.intervention_duration = QLineEdit()
        self.intervention_duration.setStyleSheet("""
            QLineEdit {
                border: 2px solid #4CAF50;
                border-radius: 10px;
                padding: 8px;
                font-size: 14px;
                font-family: 'Arial';
            }
        """)
        self.form_layout.addRow(self.duration_label, self.intervention_duration)

        self.label = QLabel("Coût journalier de base (Ar)")
        self.label.setFont(QFont("Times New Roman", 12))
        self.daily = QLineEdit()
        self.daily.setStyleSheet("""
            QLineEdit {
                border: 2px solid #4CAF50;
                border-radius: 10px;
                padding: 8px;
                font-size: 12px;
                font-family: 'Arial';
            }
        """)
        self.form_layout.addRow(self.label, self.daily)

        self.initiallabel = QLabel("Coût initial (Ar)")
        self.initiallabel.setFont(QFont("Times New Roman", 12))
        self.initial = QLineEdit()
        self.initial.setStyleSheet("""
            QLineEdit {
                border: 2px solid #4CAF50;
                border-radius: 10px;
                padding: 8px;
                font-size: 12px;
                font-family: 'Arial';
            }
        """)
        self.form_layout.addRow(self.initiallabel, self.initial)

        # Bouton avec style personnalisé
        self.simulate_button = QPushButton("Simuler")
        self.simulate_button.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: 2px solid #4CAF50;
                border-radius: 12px;
                padding: 8px 16px;
                font-size: 14px;
                font-family: 'Arial';
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QPushButton:pressed {
                background-color: #3e8e41;
            }
        """)
        self.layout.addWidget(self.simulate_button)

        self.result_label = QLabel()
        self.layout.addWidget(self.result_label)

        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)
        self.layout.addWidget(self.canvas)

        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)

    def plot_simulation(self, t_values, values):
        self.ax.clear()
        self.ax.plot(t_values, values, label="Coût accumulé")
        self.ax.set_title("Évolution du coût d'une intervention")
        self.ax.set_xlabel("Jours")
        self.ax.set_ylabel("Coût (Ar)")
        self.ax.legend()
        self.ax.grid(True)
        self.canvas.draw()

    def show_coordinates(self, event):
        if event.inaxes:
            x = event.xdata
            y = event.ydata
            self.statusBar.showMessage(f"Coordonnées : Jour(s)= {x:.2f}, Coût = {y:.2f}")
