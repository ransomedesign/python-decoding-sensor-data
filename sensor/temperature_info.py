from house_info import HouseInfo
from datetime import date


class TemperatureData(HouseInfo):
    """
    Inherits from the HouseInfo class.
    """

    def _convert_data(self, data):
        """
        Convert data using base 10
        """
        recs = []
        for rec in data:
            recs.append(int(rec, base=10))

        return recs

    def get_data_by_area(self, rec_area=0):
        """
        Overwrite method from the parent class.
        the default value of 0 means all records.
        """
        # Call parent method.
        recs = super().get_data_by_area("temperature", rec_area)

        # recs = super(HouseInfo, self)
        # recs("temperature", rec_area)
        return self._convert_data(recs)

    def get_data_by_date(self, rec_date=date.today()):
        recs = super().get_data_by_date("temperature", rec_date)

        return self._convert_data(recs)
