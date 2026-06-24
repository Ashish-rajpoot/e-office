from dataclasses import dataclass
import time


@dataclass
class Step:
    action: callable
    delay: int = 0

class WorkflowRunner:

    @staticmethod
    def run(steps):
        for step in steps:
            try:
                print(f"Running: {step.action.__name__}")
                step.action()

                if step.delay:
                    time.sleep(step.delay)

            except Exception as e:
                raise Exception(
                    f"Workflow failed at {step.action.__name__}: {e}"
                )