import datetime

from django.test import TestCase

from experimenter.experiments.tests.factories import (
    ExperimentFactory,
    ExperimentControlFactory,
    ExperimentVariantFactory,
)
from experimenter.experiments.serializers import (
    JSTimestampField,
    ExperimentVariantSerializer,
    ExperimentControlSerializer,
    ExperimentSerializer,
)


class TestJSTimestampField(TestCase):

    def test_field_serializes_to_js_time_format(self):
        field = JSTimestampField()
        example_datetime = datetime.datetime(2000, 1, 1, 1, 1, 1, 1)
        self.assertEqual(
            field.to_representation(example_datetime), 946688461000.0)

    def test_field_returns_none_if_no_datetime_passed_in(self):
        field = JSTimestampField()
        self.assertEqual(field.to_representation(None), None)


class TestExperimentVariantSerializer(TestCase):

    def test_serializer_outputs_expected_schema(self):
        variant = ExperimentVariantFactory.create()
        serialized = ExperimentVariantSerializer(variant)
        self.assertEqual(serialized.data, {
            'slug': variant.slug,
            'experiment_variant_slug': variant.experiment_variant_slug,
            'threshold': float(variant.threshold),
            'value': variant.value,
        })


class TestExperimentControlSerializer(TestCase):

    def test_serializer_outputs_expected_schema(self):
        control = ExperimentControlFactory.create()
        serialized = ExperimentControlSerializer(control)
        self.assertEqual(serialized.data, {
            'slug': control.slug,
            'experiment_variant_slug': control.experiment_variant_slug,
            'value': control.value,
        })


class TestExperimentSerializer(TestCase):

    def test_serializer_outputs_expected_schema(self):
        experiment = ExperimentFactory.create_with_variants()
        serialized = ExperimentSerializer(experiment)
        self.assertEqual(serialized.data, {
            'active': experiment.active,
            'name': experiment.name,
            'slug': experiment.slug,
            'addon_versions': experiment.addon_versions,
            'start_date': JSTimestampField().to_representation(
                experiment.start_date),
            'end_date': JSTimestampField().to_representation(
                experiment.end_date),
            'variant': ExperimentVariantSerializer(experiment.variant).data,
            'control': ExperimentControlSerializer(experiment.control).data,
        })
