class VeryPowerHungryResource:
    def open(self):
        print("Resource was opened")

    def close(self):
        print("Resource was closed")

    def do_work(self):
        print("Resource doing some work...")


# 1. Try - finally.
def main():
    res_inst = VeryPowerHungryResource()
    res_inst.open()
    try:
        res_inst.do_work()
    except:
        pass
    finally:
        res_inst.close()


# 2. Class context manager.
def main():
    class My_context_manager:
        def __init__(self):
            self.res_inst = VeryPowerHungryResource()

        def __enter__(self):
            self.res_inst.open()
            return self.res_inst

        def __exit__(self, exc_type, exc_val, exc_tb):
            self.res_inst.close()
            return True

    with My_context_manager() as resource:
        resource.do_work()


# 3. Function context manager.
from contextlib import contextmanager  # Usually this line should be at the top


def main():
    @contextmanager
    def my_context_manager_2():
        res_inst = VeryPowerHungryResource()
        res_inst.open()
        try:
            yield res_inst
        except:
            pass
        finally:
            res_inst.close()

    with my_context_manager_2() as resource:
        resource.do_work()


if __name__ == "__main__":
    main()
