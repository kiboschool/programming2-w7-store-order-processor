import unittest
from jukebox import Jukebox


class TestStoreOrderProcessor(unittest.TestCase):
    def test_init_paused(self):
        player = Jukebox(songs)
        assert player.current_state() == "Paused"

    def test_play(self):
        player = Jukebox(songs)
        player.play()
        assert player.current_state() == "Playing: Kuna Kuna"

    def test_pause(self):
        player = Jukebox(songs)
        player.play()
        player.pause()
        assert player.current_state() == "Paused"

    def test_next(self):
        player = Jukebox(songs)
        player.play()
        player.next()
        assert player.current_state() == "Playing: Herawa Ni"

    def test_previous_wrap(self):
        player = Jukebox(songs)
        player.play()
        player.previous()
        assert player.current_state() == "Playing: Wanjapi"

    def test_next_next_prev(self):
        player = Jukebox(songs)
        player.play()
        player.next()
        player.next()
        player.previous()
        assert player.current_state() == "Playing: Herawa Ni"

    def test_next_wrap(self):
        player = Jukebox(songs)
        player.play()
        for i in range(len(songs)):
            player.next()
        player.next()
        assert player.current_state() == "Playing: Herawa Ni"

if __name__ == "__main__":
    unittest.main()
