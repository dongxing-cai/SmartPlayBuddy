import asyncio
import websockets
import hashlib
import json
import Xbox

# 转译Xbox操作
class XboxGamepad(Xbox.Gamepad):
    def operator(self, operators):
        for operator in operators:
            if operator["type"] == "button":
                if operator["operator"] == "press":
                    eval("self." + operator["button"] + "()")
                elif operator["operator"] == "release":
                    eval("self." + operator["button"] + "_()")
            elif operator["type"] == "joystick":
                if operator["axis"] == "left":
                    self.LEFT_JOYSTICK(operator["x"], operator["y"])
                elif operator["axis"] == "right":
                    self.RIGHT_JOYSTICK(operator["x"], operator["y"])
            elif operator["type"] == "reset":
                self.RESET()

class Client:
    def __init__(self, uri: str, authentication: dict):
        self.uri = uri
        authentication['password'] = hashlib.sha256(authentication['password'].encode('utf-8')).hexdigest()
        self.authentication = authentication
        self.devices = {}
        try:
            asyncio.run(self.client())
        except KeyboardInterrupt:
            print("已关闭")

    # 连接至服务器
    async def client(self):
            try:
                async with websockets.connect(self.uri) as websocket:
                    # 发送验证信息
                    await websocket.send(json.dumps(self.authentication))
                    # 接收并处理消息
                    await self.receive(websocket)
            except TimeoutError:
                print("连接超时")
            except ConnectionRefusedError:
                print("无法连接到服务器，请确保服务器已运行")
            except websockets.exceptions.ConnectionClosed as e:
                if e.code != 1000:
                    print(f"连接关闭：代码=\033[4;33m{e.code}\033[0m，原因=\033[4;33m{e.reason}\033[0m")
            except websockets.exceptions.ConnectionClosedError:
                print("与服务器的连接已关闭")

    # 接收并处理消息
    async def receive(self, websocket):
        try:
            while True:
                # 从服务器接收信息
                response = await websocket.recv()
                # 解码
                if type(response) is bytes:
                    common = json.loads(response)
                    commander = common["commander"]
                    del common["commander"]
                    # 尝试执行命令
                    try:
                        # 添加设备
                        if common["type"] == "AddDevice":
                            if common["device"] == "Xbox":
                                self.devices[common["name"]] = XboxGamepad()
                        # 操作设备
                        elif common["type"] == "OperateDevice":
                            if self.devices[common["name"]].__class__.__name__ == "XboxGamepad":
                                self.devices[common["name"]].operator(common["operators"])
                        # 移除设备
                        elif common["type"] == "RemoveDevice":
                            del self.devices[common["name"]]
                        else:
                            await websocket.send(
                                json.dumps({"type": "Send", "device": commander, "error": common}))
                            print(f"\033[4;33m{response}\033[0m")
                    except:
                        await websocket.send(
                            json.dumps({"type": "Send", "device": commander, "error": common}))
                        print(f"\033[4;33m{response}\033[0m")
                elif type(response) is str:
                    print(response)
        except ConnectionRefusedError:
            print("无法连接到服务器，请确保服务器已运行")
        except websockets.exceptions.ConnectionClosed as e:
            if e.code != 1000:
                print(f"连接关闭：代码=\033[4;33m{e.code}\033[0m，原因=\033[4;33m{e.reason}\033[0m")
        except websockets.exceptions.ConnectionClosedError:
            print("与服务器的连接已关闭")

if __name__ == "__main__":
    uri = "ws://smtplay.cabyss.cn:2508/server/ws"
    authentication = {"type": "client", "username": "test", "password": "123456", "devicename": "test_device"}
    client = Client(uri, authentication)