import asyncio
import websockets
import hashlib
import json

class Mod:
    def __init__(self, uri: str, authentication: dict, task=None):
        self.uri = uri
        authentication['password'] = hashlib.sha256(authentication['password'].encode('utf-8')).hexdigest()
        self.authentication = authentication
        if task:
            self._task = task
        self.websocket = None
        asyncio.run(self.mod())

    # 连接至服务器
    async def mod(self):
        try:
            async with websockets.connect(self.uri) as websocket:
                # 发送验证信息
                await websocket.send(json.dumps(self.authentication))
                # 接收并处理消息
                asyncio.create_task(self.receive(websocket))
                # 永久阻塞
                self.future = asyncio.Future()
                try:
                    await self.future
                except asyncio.CancelledError:
                    print("已关闭")

        except TimeoutError:
            print("连接超时")
        except ConnectionRefusedError:
            print("无法连接到服务器，请确保服务器已运行")
        except websockets.exceptions.ConnectionClosed as e:
            if e.code != 1000:
                print(f"连接关闭：代码=\033[4;33m{e.code}\033[0m，原因=\033[4;33m{e.reason}\033[0m")
        except websockets.exceptions.ConnectionClosedError:
            print("与服务器的连接已关闭")
        finally:
            # 取消阻塞
            try:
                self.future.cancel()
            except AttributeError:
                pass

    async def receive(self, websocket):
        try:
            self.websocket = websocket
            while True:
                # 从服务器接收信息
                response = await websocket.recv()
                # 解码
                if type(response) is bytes:
                    task = json.loads(response)
                    print(f'\033[1;32m{task["operator"]["username"]}: {task}\033[0m')
                    # 尝试执行任务
                    try:
                        asyncio.create_task(self._task(websocket, task))
                    except:
                        await websocket.send(json.dumps({"type": "Send", "user": task["operator"]["username"], "device": task["operator"]["devicename"], "error": task}))
                        print(f"\033[4;33m{response}\033[0m")
                elif type(response) is str:
                    print(f'\033[1;34m{response}\033[0m')
        except ConnectionRefusedError:
            print("无法连接到服务器，请确保服务器已运行")
        except websockets.exceptions.ConnectionClosed as e:
            if e.code != 1000:
                print(f"连接关闭：代码=\033[4;33m{e.code}\033[0m，原因=\033[4;33m{e.reason}\033[0m")
        except websockets.exceptions.ConnectionClosedError:
            print("与服务器的连接已关闭")
        finally:
            # 取消阻塞
            self.future.cancel()

    @staticmethod
    async def _task(websocket, task):
        operate = {"type": "Send", "user": task["operator"]["username"], "commander": task["operator"]["devicename"],"device": task["device"], "command": task["task"]}
        await websocket.send(json.dumps(operate))


if __name__ == "__main__":
    uri = "ws://smtplay.cabyss.cn:2508/server/ws"
    authentication = {"type": "mod", "username": "test", "password": "123456", "modname": "test_mod", "description": "This is a test mod."}
    mod = Mod(uri, authentication)