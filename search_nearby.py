import googlemaps
api_key = ''			#api key required



# get_lat_lng(gmaps:google maps client object,address: place to search as string)
def get_lat_lng(gmaps,address):
    lat = gmaps.geocode(address)[0]['geometry']['location']['lat']
    lng = gmaps.geocode(address)[0]['geometry']['location']['lng']
    return (lat,lng)
    
    
    
# get_nearby_places(gmaps:google maps client object ,loc: location as tuple,keyword: to search,n: number of results)
def get_nearby_places(gmaps,loc,keyword,n):
    nearby_places = gmaps.places_nearby(loc,None,keyword,None,None,None,None,None,"distance")
    nearby_coordinates = []
    for each in range(n):
        lat = nearby_places['results'][each]['geometry']['location']['lat']
        lng = nearby_places['results'][each]['geometry']['location']['lng']
        nearby_coordinates.append(tuple((lat,lng)))
    return nearby_coordinates
    
    
    
# function to fetch location name from the location 
def get_loc_name(locs,gmaps):
    for loc in locs:
        print(gmaps.reverse_geocode(loc)[0]['formatted_address'])
        
        
def main():
    gmaps = googlemaps.Client(api_key)
    
    cur_location = get_lat_lng(gmaps,"brookfield hospital Bengaluru")

    nearby = get_nearby_places(gmaps,cur_location,"drycleaner",3)
    
    get_loc_name(nearby,gmaps)
    
	# one liner 
	#  get_loc_name(get_nearby_places(gmaps,get_lat_lng(gmaps,"brookfield hospital Bengaluru"),"drycleaner",3),gmaps)
    
    
if __name__ =='__main__':
    main()