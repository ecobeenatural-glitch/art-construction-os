class Pipeline:

    def __init__(self):
        self.steps = []

    def add(self, step):
        self.steps.append(step)

    def run(self, context):
        for step in self.steps:
            print(f"Running {step.__class__.__name__}")
            step.run(context)