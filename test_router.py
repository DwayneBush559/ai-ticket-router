import unittest

from router import route_ticket


class TicketRouterTests(unittest.TestCase):
    def test_security_ticket(self):
        result = route_ticket("Suspicious login and phishing email hit my account")
        self.assertEqual(result.category, "security")
        self.assertIn("phishing", result.matched_terms)

    def test_network_ticket(self):
        result = route_ticket("VPN connection is offline and wifi is slow")
        self.assertEqual(result.category, "network")

    def test_unknown_ticket_falls_back(self):
        result = route_ticket("Please help with my desk reservation")
        self.assertEqual(result.category, "general")
        self.assertEqual(result.confidence, 0.0)


if __name__ == "__main__":
    unittest.main()
