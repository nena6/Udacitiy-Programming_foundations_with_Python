import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story", 124, "A story of a boy and his toys that "
                                      "come to life.",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg",
                        "https://www.google.hr/url?sa=t&rct=j&q=&esrc=s&source=web&cd=2&cad=rja&uact=8&ved=0ahUKEwiE4dHX-PzXAhWrDZoKHa3fCdcQtwIINjAB&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DKYz2wyBy3kc&usg=AOvVaw0z39p4CAtfAw4uZDhaE4vX")

avatar = media.Movie("Avatar", 136, "A marine on an alien planet.",
                     "https://upload.wikimedia.org/wikipedia/hr/thumb/5/55/Avatar_2009.jpg/220px-Avatar_2009.jpg", "https://www.google.hr/url?sa=t&rct=j&q=&esrc=s&source=web&cd=2&cad=rja&uact=8&ved=0ahUKEwj666bbj4fYAhUqCpoKHVdAA3AQtwIILTAB&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3D5PSNL1qE6VY&usg=AOvVaw04HYX6vYPNfKceWOFgCZ2H")

seinfield = media.TvShow("Seinfield", 28, 4, 2, "HBO")

print(toy_story.title)
#print(avatar.storyline)
#avatar.show_trailer()
print(seinfield.title + str(seinfield.season))
movies = [toy_story, avatar]
#fresh_tomatoes.open_movies_page(movies)

print(media.Movie.VALID_RATINGS)
print("doc: " + media.Movie.__doc__)
#print("dict: " + media.Movie.__dict__)
print("module: " + media.Movie.__module__)
print("name: " + media.Movie.__name__)
