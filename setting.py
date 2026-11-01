class Setting():
    def __init__(self):
        # general setting
        self.screenWidth = 1280
        self.screenHeight = 720
        self.caption = 'Alien Invasion'

        # ship setting
        self.shipSpeed = 1
        self.shipLives = 3

        # bullet setting
        self.bulletSpeed = 1
        self.bulletDelay = 1

        # alien setting
        self.alienSpeed = 0.03
        self.dropSpeed = 15
        # 1 = right, -1 = left
        self.fleetDirection = 1

        # sound
        self.pew = 'sound/pew.wav'
        self.boom = 'sound/boom.wav'
        self.wow = 'sound/wow.wav'
        self.fail = 'sound/fail.wav'

        # explosion
        self.explosion = 'pic/explode.gif'

        # speed up after next level
        self.speedUp = 1.1

        self.scaleSpeed()
    
    def scaleSpeed(self):
        self.shipSpeed *= self.speedUp
        self.bulletSpeed *= self.speedUp
        self.alienSpeed *= self.speedUp
    
    def reset(self):
        self.shipSpeed = 0.07
        self.bulletSpeed = 1
        self.alienSpeed = 0.03