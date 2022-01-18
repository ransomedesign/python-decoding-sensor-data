from house_info import HouseInfo
from datetime import date


class EnergyData(HouseInfo):
    # Constants.
    ENERGY_PER_BULB = 0.2
    ENERGY_BITS = 0x0F0

    def _get_energy(self, rec):
        # Convert to an integer to which you can apply bitwise operations.
        energy = int(rec, base=16)
        # No idea.
        energy = energy & self.ENERGY_BITS
        # Shift by 4 bits.
        energy = energy >> 4
        return energy

    def _convert_data(self, data):
        recs = []
        for rec in data:
            recs.append(self._get_energy(rec))
        return recs

    def get_data_by_area(self, rec_area=0):
        recs = super().get_data_by_area("energy_usage", rec_area)
        return self._convert_data(recs)

    def get_data_by_date(self, rec_date=date.today()):
        recs = super().get_data_by_date("energy_usage", rec_date)
        return self._convert_data(recs)

    def calculate_energy_usage(self, data):
        """
        Take list of energy usage values, calculate the cost per light bulb
        usage.
        """

        # The list comprehension should use field as the expression variable.
        # The field variable should be multiplied by the ENERGY_PER_BULB
        # constant.

        # List comprehension.

        total_energy = sum([field * self.ENERGY_PER_BULB for field in data])

        return total_energy
