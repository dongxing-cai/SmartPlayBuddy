import vgamepad

class Gamepad:
    def __init__(self):
        self.gamepad = vgamepad.VX360Gamepad()
        self.RESET()



    def LEFT_JOYSTICK(self, x=0, y=0):
        self.gamepad.left_joystick_float(x, y)
        self.gamepad.update()

    def LS(self):
        self.gamepad.press_button(vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB)
        self.gamepad.update()

    def LS_(self):
        self.gamepad.release_button(vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB)
        self.gamepad.update()


    def UP(self):
        self.gamepad.press_button(vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP)
        self.gamepad.update()

    def DOWN(self):
        self.gamepad.press_button(vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)
        self.gamepad.update()

    def LEFT(self):
        self.gamepad.press_button(vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT)
        self.gamepad.update()

    def RIGHT(self):
        self.gamepad.press_button(vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT)
        self.gamepad.update()

    def UP_(self):
        self.gamepad.release_button(vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP)
        self.gamepad.update()

    def DOWN_(self):
        self.gamepad.release_button(vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)
        self.gamepad.update()

    def LEFT_(self):
        self.gamepad.release_button(vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT)
        self.gamepad.update()

    def RIGHT_(self):
        self.gamepad.release_button(vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT)
        self.gamepad.update()


    def RIGHT_JOYSTICK(self, x=0, y=0):
        self.gamepad.right_joystick_float(x, y)
        self.gamepad.update()

    def RS(self):
        self.gamepad.press_button(vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB)
        self.gamepad.update()

    def RS_(self):
        self.gamepad.release_button(vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB)
        self.gamepad.update()


    def A(self):
        self.gamepad.press_button(vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_A)
        self.gamepad.update()

    def B(self):
        self.gamepad.press_button(vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_B)
        self.gamepad.update()

    def X(self):
        self.gamepad.press_button(vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_X)
        self.gamepad.update()

    def Y(self):
        self.gamepad.press_button(vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_Y)
        self.gamepad.update()

    def A_(self):
        self.gamepad.release_button(vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_A)
        self.gamepad.update()

    def B_(self):
        self.gamepad.release_button(vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_B)
        self.gamepad.update()

    def X_(self):
        self.gamepad.release_button(vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_X)
        self.gamepad.update()

    def Y_(self):
        self.gamepad.release_button(vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_Y)
        self.gamepad.update()


    def BACK(self):
        self.gamepad.press_button(vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_BACK)
        self.gamepad.update()

    def GUIDE(self):
        self.gamepad.press_button(vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_GUIDE)
        self.gamepad.update()

    def START(self):
        self.gamepad.press_button(vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_START)
        self.gamepad.update()

    def BACK_(self):
        self.gamepad.release_button(vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_BACK)
        self.gamepad.update()

    def GUIDE_(self):
        self.gamepad.release_button(vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_GUIDE)
        self.gamepad.update()

    def START_(self):
        self.gamepad.release_button(vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_START)
        self.gamepad.update()


    def LB(self):
        self.gamepad.press_button(vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER)
        self.gamepad.update()

    def LB_(self):
        self.gamepad.release_button(vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER)
        self.gamepad.update()

    def LT(self, value=1):
        self.gamepad.left_trigger_float(value)
        self.gamepad.update()

    def LT_(self):
        self.gamepad.left_trigger_float(0)
        self.gamepad.update()


    def RB(self):
        self.gamepad.press_button(vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER)
        self.gamepad.update()

    def RB_(self):
        self.gamepad.release_button(vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER)
        self.gamepad.update()

    def RT(self, value=1):
        self.gamepad.right_trigger_float(value)
        self.gamepad.update()

    def RT_(self):
        self.gamepad.right_trigger_float(0)
        self.gamepad.update()


    def RESET(self):
        self.gamepad.reset()
        self.gamepad.update()



    def __del__(self):
        del self.gamepad