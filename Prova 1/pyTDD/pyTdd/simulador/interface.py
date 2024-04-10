# Importação das bibliotecas
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PyQt5.QtCore import QTimer
import random


class UmidadeMonitor(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()
        self.dataLabel = QLabel("Aguardando dados...", self)
        self.layout.addWidget(self.dataLabel)
        self.setLayout(self.layout)
        self.setGeometry(300, 300, 600, 100)  # Tamanho da janela
        self.setWindowTitle('Monitor de Umidade')
        # Timer para atualização automática dos dados
        self.timer = QTimer(self)
        # Conecta o timeout do timer à função de atualização dos dados
        self.timer.timeout.connect(self.updateData)
        self.timer.start(5000)  # Intervalo de 5 segundos para publicação

    def updateData(self):
        sensor_id, sensor_type, humidity, alerta = self.generateData()
        self.dataLabel.setText(
            f"Sensor {sensor_id}: {sensor_type} | "
            "Umidade: {humidity:.2f}%{alerta}"
        )

    def generateData(self):
        sensor_id = f"{random.randint(1,3)}-{random.randint(1,5)}"
        sensor_type = random.choice(["Hortaliças", "Flores"])
        humidity = random.uniform(20, 90)
        alerta = self.checkAlert(sensor_type, humidity)
        return sensor_id, sensor_type, humidity, alerta

    # Função de alertas
    def checkAlert(self, sensor_type, humidity):
        if sensor_type == "Hortaliças":
            if humidity < 30:
                return " [ALERTA: Umidade MUITO BAIXA!]"
            elif humidity > 70:
                return " [ALERTA: Umidade MUITO ALTA!]"
        elif sensor_type == "Flores":
            if humidity < 40:
                return " [ALERTA: Umidade MUITO BAIXA!]"
            elif humidity > 80:
                return " [ALERTA: Umidade MUITO ALTA!]"
        return ""  # Retorna uma string vazia se não houver alerta

    def main():
        app = QApplication(sys.argv)
        ex = UmidadeMonitor()
        ex.show()
        sys.exit(app.exec_())

    if __name__ == '__main__':
        main()
