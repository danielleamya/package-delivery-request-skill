from mycroft import MycroftSkill, intent_file_handler


class PackageDeliveryRequest(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('request.delivery.package.intent')
    def handle_request_delivery_package(self, message):
        self.speak_dialog('request.delivery.package')


def create_skill():
    return PackageDeliveryRequest()

