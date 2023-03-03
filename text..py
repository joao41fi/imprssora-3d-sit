import pronsole 

pr = pronsole.Pronsole('/dev/ttyACM0', 250000)  # substitua /dev/ttyACM0 pela porta serial que você está usando
pr.connect()
pr.send_now("G28")
