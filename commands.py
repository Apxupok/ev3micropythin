#Операторы
if a>b: #Сравниваем a и b
  print("a больше b")
else:
  print("b больше a")

while a>b: #Запускаем цикл, который делает что-то, пока а и не станет меньше b
  print("Пока что a больше b")
  
for i in range(10): #Цикл который перебирает значения от 0 до 9 включительно
  print(i)


#Мотор
motor_b = Motor(Port.B) #Объявляем мотор
motor_b.run(700) #Просто запускаем мотор с мощностью 700, не забываем про wait()
motor_b.run_time(600, 3000) #Запускаем мотор с мощностью 600 на 3 секунды
motor_b.run_target(960,90) #Запускаем мотор с мощностью 960 в 90 градусов, помним, что мотор при запуске запоминает все повороты, поэтому надо сбрасывать
motor_b.run_angle(960,90)  #Запускаем мотор с мощностью 960 на 90 градусов, отличает от пред. команды тем, что поворачивает на угол, а не в угол, сбрасывать не обязательно
motor_b.reset_angle(0)  #Сбрасываем угол у мотора в 0
motor_b.angle() # Считываем угол
motor_b.brake() 
motor_b.hold()


#Смарт хаб
#Звук
ev3.speaker.beep() # Сигнал 
#Кнопки
ev3.buttons.pressed() == [Button.UP] # проверяем нажата ли кнопука "вверх"
#Экран
ev3.screen.clear()  #Очиащаем экран
ev3.screen.draw_text(75, 10, x)  # Выводим текст на экра в координаты по х 75 по у 10
ev3.screen.draw_circle(x, y, r, fill=True)  #Рисуем круг, который заполнен цветом
ev3.screen.draw_line(x1,y1,x2,y2)  #Рисуем линию от точки(х1 у1) до точки (х2 у2)
#Цвет подсветки
ev3.light.on(Color.ORANGE)
ev3.light.on(Color.GREEN)
ev3.light.on(Color.RED)
ev3.light.off()

#Датчики
touch = TouchSensor(Port.S1) #Объявляем датчки касания
touch.pressed() #Дает значение true или false. Применяется в условиях 
if touch.pressed():
  print("Ты нажал меня")
  
gyro = GyroSensor(Prort.S1)#Объявляем датчик наклона, гироскоп
gyro.reset_angle(0)
gyro.angle() #Считываем угол наклона датчика, тут хранится число, которое высчитывает сейчас датчик
 
ultra = UltrasonicSensor(Port.S1) #Объявляем датчик расстояния
ultra.distance() #Считываем расстояние, тут хранится число, которое высчитывает сейчас датчик расстояния

color = ColorSensor(Port.S3) #Объявляем датчик цвета
if color_.color() == Color.RED:


