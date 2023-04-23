# Explicação do código

Começamos com a adição do interpretador:
```
#!/usr/bin/env python3
```

Importamos rclpy (nos permite criar comunicação ros2 por meio do pyhton), Node (nó do ros2) e Twist (tipo de dado que é enviado na nossa comunicação)
```
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
```

Criamos o nosso nó Draw herdando a classe Node com três métodos: movement1, movement2 e send_pub_vel.
```
class Draw(Node):

    def __init__(self):
        super().__init__("draw")
        self.pub_vel_ = self.create_publisher(Twist, "/turtle1/cmd_vel", 10)
        self.timer_ = self.create_timer(2.0, self.send_pub_vel)
        self.part = 1
        self.msg = Twist()
        self.get_logger().info("Drawing...")

    def movement1(self):
        self.msg.linear.x = 2.0
        self.msg.angular.z = 2.0
        self.pub_vel_.publish(self.msg)

    def movement2(self):
        self.msg.linear.x = -3.0
        self.msg.angular.z = 3.0
        self.pub_vel_.publish(self.msg)

    def send_pub_vel(self):
        if self.part == 1:
            self.movement1()
            self.part += 1

        else:
            self.movement2()
            self.part -= 1
```

Mas, primeiro, começamos pelo init, onde criamos um publicador que recebe o tipo de dado Twist, o tópico onde ele deverá ser publicado e a quantidade de espaço disponível para a mensagem, depois um timer que executa o método send_pub_vel a cada quantidade de tempo determinada, uma variável para guardar qual movimento está sendo realizado, uma variável para a mensagem e um método para escrever que o processo foi iniciado. 
```
def __init__(self):
    super().__init__("draw")
    self.pub_vel_ = self.create_publisher(Twist, "/turtle1/cmd_vel", 10)
    self.timer_ = self.create_timer(2.0, self.send_pub_vel)
    self.part = 1
    self.msg = Twist()
    self.get_logger().info("Drawing...")
```
Após, definimos como serão os dois movimentos que serão realizados pela tartaruga, eles recebem um valor para movimentação angular e um para linear, depois, publicam esses valores na mensagem.
```
def movement1(self):
    self.msg.linear.x = 2.0
    self.msg.angular.z = 2.0
    self.pub_vel_.publish(self.msg)

def movement2(self):
    self.msg.linear.x = -3.0
    self.msg.angular.z = 3.0
    self.pub_vel_.publish(self.msg) 
```
Criamos um método que executa o movimento de acordo com o número na variável, alternando entre o movimento 1 e 2.
```
def send_pub_vel(self):
    if self.part == 1:
      self.movement1()
      self.part += 1

    else:
      self.movement2()
      self.part -= 1
```

Depois a função main que inicia o rclpy, mantém o nó rodando várias vezes e não apenas uma com o método spin e depois mata o nó com o método shutdown.
```
def main(args=None):
    rclpy.init(args=args)
    node = Draw()
    rclpy.spin(node)
    rclpy.shutdown()
```
