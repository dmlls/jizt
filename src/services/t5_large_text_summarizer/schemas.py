# Copyright (C) 2021 Diego Miguel Lozano <dml1001@alu.ubu.es>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# For license information on the libraries used, see LICENSE.

"""Marshmallow Schemas for TextSummarizerService."""

from marshmallow import Schema, fields

__version__ = '0.1.3'


class JSONSerializableBytesField(fields.Field):
    """A JSON serializable :obj:`bytes` field.

    For more info, see the
    `Marshmallow docs <https://marshmallow.readthedocs.io/en/stable/marshmallow.fields.html>`__.
    """

    def _serialize(self, value, attr, obj, **kwargs):
        """Serialize :obj:`bytes` to :obj:`string`.

        For more info, see base class.
        """

        if value is None:
            return None
        return value.decode('latin1')

    def _deserialize(self, value, attr, data, **kwargs):
        """Deserialize :obj:`bytes` from :obj:`str`.

        For more info, see base class.
        """

        if isinstance(value, str):
            return value.encode('latin1')
        raise super(JSONSerializableBytesField,
                    self).make_error('Value must be a string.')


class TextSummarizationConsumedMsgSchema(Schema):
    """Schema for the consumed messages from the topic :attr:`KafkaTopic.TEXT_SUMMARIZATION`.

    Fields:
        text_encodings (:obj:`JSONSerializableBytesField`):
            The encoded text to be summarized.
    """

    text_encodings = JSONSerializableBytesField(required=True)


class TextPostprocessingProducedMsgSchema(Schema):
    """Schema for the produced messages to the topic :attr:`KafkaTopic.TEXT_POSTPROCESSING`.

    Fields:
        summary (:obj:`str`):
            The generated summary.
    """

    summary = fields.Str(required=True)