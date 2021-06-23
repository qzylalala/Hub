from hub.core.meta.encode.byte_positions import BytePositionsEncoder
from hub.core.meta.encode.shape import ShapeEncoder


class Chunk:
    def __init__(self, min_size_target: int, max_size: int):
        self.min_size_target = min_size_target
        self.max_size = max_size

        self._shape_encoder = ShapeEncoder()
        self._byte_positions_encoder = BytePositionsEncoder()  # TODO

        self._data = bytearray()

    @property
    def has_space(self):
        return len(self._data) < self.min_size_target

    def extend(self, buffer: bytes, num_samples: int):
        # TODO: encode start byte / end byte
        if not self.has_space:
            # TODO: exceptions.py
            raise Exception("This chunk does not have space left.")

        buffer_length = len(buffer)

        if buffer_length % num_samples != 0:
            # TODO: exceptions.py
            raise Exception(
                f"Buffer length must be divisible by `num_samples`. {buffer_length} % {num_samples} != 0"
            )

        num_bytes_per_sample = buffer_length // num_samples
        self._data.extend(buffer)
        self._byte_positions_encoder.add_byte_position(
            num_bytes_per_sample, num_samples
        )