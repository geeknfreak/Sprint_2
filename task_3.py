class PointsForPlace:
    def get_points_for_place(self, place):
        self.place = place
        if self.place > 100:
            print('Баллы начисляются только первым 100 участникам')
            return 0
        elif self.place < 1:
            print('Спортсмен не может занять нулевое или отрицательное место')
            return 0
        else: 
            points =  101 - place
            return points

class PointsForMeters:
    def get_points_for_meters(self, meters):
        self.meters = meters
        if self.meters < 0:
            print('Количество метров не может быть отрицательным')
            return 0
        else: 
            points =  0.5 * meters
            return int(points)
            

class TotalPoints(PointsForPlace, PointsForMeters):
    def get_total_points(self, place, meters):
        point_for_meters = self.get_points_for_meters(meters)
        point_for_place = self.get_points_for_place(place)
        return point_for_meters + point_for_place

    


points_for_place = PointsForPlace()
print(points_for_place.get_points_for_place(10))

points_for_meters = PointsForMeters()
print(points_for_meters.get_points_for_meters(10))

total_points = TotalPoints()
print(total_points.get_points_for_place(10))
print(total_points.get_points_for_meters(10))
print(total_points.get_total_points(100, 10))