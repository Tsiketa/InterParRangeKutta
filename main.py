import sys
from PyQt5.QtWidgets import QApplication
from app.controller.simulationModel import SimulationController 
from app.view.simulationView import SimulationView
from app.model.simulationModel import SimulationModel
if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Initialisation du modèle, de la vue, et du contrôleur
    #cc= CostSimulationController()
    model = SimulationModel(0, 0)
    view = SimulationView()
    controller = SimulationController(model, view)

    view.show()
    sys.exit(app.exec_())
