from com.py.actions.commands import Commands


class Controller:

    @staticmethod
    def commence():
        while True:
            if not Commands().get_input():
                break
        return


initiator = Controller()
initiator.commence()
