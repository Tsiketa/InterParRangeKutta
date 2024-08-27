
class SimulationController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        # Connexion des signaux et des slots
        self.view.simulate_button.clicked.connect(self.run_simulation)
        self.view.canvas.mpl_connect("motion_notify_event", self.view.show_coordinates)

    def run_simulation(self):
        try:
            # Récupération des valeurs des paramètres depuis la vue
            duration = int(self.view.intervention_duration.text())
            daily = float(self.view.daily.text())
            initial = float(self.view.initial.text())

            if duration <= 0 or daily<= 0:
                self.view.result_label.setText("Veuillez entrer des valeurs valides.")
                return

            # Mise à jour du modèle avec les nouvelles valeurs
            self.model.daily = daily
            self.model.initial = initial

            # Exécution de la simulation
            t_values, values = self.model.run_simulation(duration)

            # Affichage du résultat dans la vue
            self.view.plot_simulation(t_values, values)
            self.view.result_label.setText(f"Simulation terminée avec succès pour une durée de {duration} jours.")

        except ValueError:
            self.view.result_label.setText("Erreur : Veuillez entrer des valeurs numériques valides.")

