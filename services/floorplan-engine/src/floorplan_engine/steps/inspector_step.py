from floorplan_engine.core.base_step import BaseStep
from floorplan_engine.drawing_inspector import DrawingInspector


class InspectorStep(BaseStep):

    def run(self, context):

        inspector = DrawingInspector(context.cropped_image)

        inspector.report()