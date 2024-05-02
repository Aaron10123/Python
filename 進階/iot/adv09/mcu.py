import network
from umqtt.simple import MQTTClient
import sys


class gpio:
    def __init__(self):
        self._D0 = 16
        self._D1 = 5
        self._D2 = 4
        self._D3 = 0
        self._D4 = 2
        self._D5 = 14
        self._D6 = 12
        self._D7 = 13
        self._D8 = 15
        self._SDD3 = 10
        self._SDD2 = 9

    @property
    def D0(self):
        return self._D0

    @property
    def D1(self):
        return self._D1

    @property
    def D2(self):
        return self._D2

    @property
    def D3(self):
        return self._D3

    @property
    def D4(self):
        return self._D4

    @property
    def D5(self):
        return self._D5

    @property
    def D6(self):
        return self._D6

    @property
    def D7(self):
        return self._D7

    @property
    def D8(self):
        return self._D8

    @property
    def SDD3(self):
        return self._SDD3

    @property
    def SDD2(self):
        return self._SDD2


class wifi:
    def __init__(self, ssid=None, password=None):
        """
        初始化 WIFI 模組
        ssid: WIFI 名稱
        password: WIFI 密碼
        """

        self.sta = network.WLAN(network.STA_IF)
        self.ap = network.WLAN(network.AP_IF)
        self.ssid = ssid
        self.password = password
        self.ap_active = False
        self.sta_active = False
        self.ip = None

    def setup(self, ap_active=False, sta_active=False):
        """
        設定 WIFI 模組
        ap_active: 是否開啟 AP 模式
        sta_active: 是否開啟 STA 模式

        使用方法:
        wi.setup(ap_active=True|False,sta_active=True|False)
        """
        self.ap_active = ap_active
        self.sta_active = sta_active
        self.ap.active(ap_active)
        self.sta.active(sta_active)

    def scan(self):
        """
        搜尋 WIFI
        返回: WIFI 列表

        使用方法:
        wi.scan()
        """
        if self.sta_active:
            wifi_list = self.sta.scan()
            print("Scan result:")
            for wifi in wifi_list:
                print(wifi[0])
        else:
            print("STA mode is not active.")

    def connect(self, ssid=None, password=None) -> bool:
        ssid = ssid if ssid is not None else self.ssid
        password = password if password is not None else self.password
        if not self.sta_active:
            print("STA 模式未啟用")
            return False

        if ssid is None or password is None:
            print("WIFI 名稱或密碼未設定")
            return False

        if self.sta_active:
            self.sta.connect(ssid, password)
            while not self.sta.isconnected():
                pass
            self.ip = self.sta.ifconfig()[0]
            print("Connected to WIFI", "IP:", self.ip)
            return True


class MQTT:
    def __init__(self, mqttClientId, mq_server, mqtt_username, mqtt_password):
        self.mq_server = mq_server
        self.mqttClientId = mqttClientId
        self.mqtt_username = mqtt_username
        self.mqtt_password = mqtt_password
        self.mqClient0 = MQTTClient(
            mqttClientId,
            mq_server,
            user=mqtt_username,
            password=mqtt_password,
            keepalive=30,
        )

    def connect(self):
        try:
            self.mqClient0.connect()
        except:
            sys.exit()
        finally:
            print("connect MQTT server")

    def subscribe(self, topic, on_message):
        self.mqClient0.set_callback(on_message)
        self.mqClient0.subscribe(topic)

    def check_msg(self):
        self.mqClient0.check_msg()
        self.mqClient0.ping()
