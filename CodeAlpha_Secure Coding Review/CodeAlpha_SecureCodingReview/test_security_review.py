
import unittest

from vulnerable_app import (
    setup_database as vulnerable_database,
    find_student as vulnerable_search
)

from secure_app import (
    setup_database as secure_database,
    find_student as secure_search
)


class SecurityComparisonTests(unittest.TestCase):

    def setUp(self):

        # Create separate databases for fair comparison
        self.vulnerable_db = vulnerable_database()
        self.secure_db = secure_database()

    def tearDown(self):

        self.vulnerable_db.close()
        self.secure_db.close()

    # ==========================================
    # TEST 1: COMPARE NORMAL SEARCH
    # ==========================================

    def test_normal_search(self):

        vulnerable_result = vulnerable_search(
            self.vulnerable_db, "rumaisa"
        )

        secure_result = secure_search(
            self.secure_db, "rumaisa"
        )

        self.assertEqual(
            vulnerable_result, secure_result
        )

        self.assertEqual(
            len(secure_result[0]), 11
        )

        print("\n[PASS] Both applications search correctly.")
        print("[PASS] All 11 student information fields returned.")

    # ==========================================
    # TEST 2: DETECT SQL INJECTION
    # IN VULNERABLE APPLICATION
    # ==========================================

    def test_vulnerable_sql_injection(self):

        malicious_input = "' OR '1'='1"

        result = vulnerable_search(
            self.vulnerable_db, malicious_input
        )

        # Verify all four student records are exposed
        self.assertEqual(len(result), 4)

        # Verify all 11 columns are exposed
        self.assertEqual(len(result[0]), 11)

        print("\n" + "!" * 55)
        print("  ERROR: SQL INJECTION VULNERABILITY DETECTED!")
        print("!" * 55)

        print("Malicious input:", malicious_input)
        print("\nUnauthorized records exposed:")

        columns = [
            "Username",
            "Full Name",
            "Email",
            "Department",
            "Phone",
            "Student ID",
            "University",
            "Semester",
            "CGPA",
            "Skills",
            "Address"
        ]

        for student in result:

            print("\n---------------- STUDENT ----------------")

            for column, value in zip(columns, student):
                print(f"{column}: {value}")

        print("\n[WARNING] All four student records exposed.")

    # ==========================================
    # TEST 3: CHECK SQL INJECTION
    # AGAINST SECURE APPLICATION
    # ==========================================

    def test_secure_sql_injection(self):

        malicious_input = "' OR '1'='1"

        result = secure_search(
            self.secure_db, malicious_input
        )

        self.assertEqual(result, [])

        print("\n" + "=" * 55)
        print("  SECURITY CORRECTION: SQL INJECTION BLOCKED")
        print("=" * 55)

        print("[PASS] No unauthorized records were exposed.")

    # ==========================================
    # TEST 4: COMPARE UNKNOWN USERNAME
    # ==========================================

    def test_unknown_username(self):

        vulnerable_result = vulnerable_search(
            self.vulnerable_db, "unknown"
        )

        secure_result = secure_search(
            self.secure_db, "unknown"
        )

        self.assertEqual(vulnerable_result, [])
        self.assertEqual(secure_result, [])

        print("\n[PASS] Both applications handle unknown users.")

    # ==========================================
    # TEST 5: SECURE APP REJECTS EMPTY INPUT
    # ==========================================

    def test_secure_empty_input(self):

        with self.assertRaises(ValueError):
            secure_search(self.secure_db, "")

        print("\n[PASS] Empty input rejected.")

    # ==========================================
    # TEST 6: SECURE APP REJECTS LONG INPUT
    # ==========================================

    def test_secure_long_input(self):

        with self.assertRaises(ValueError):
            secure_search(self.secure_db, "a" * 51)

        print("\n[PASS] Excessively long input rejected.")


# ==========================================
# MAIN TEST RUNNER
# ==========================================

if __name__ == "__main__":

    print("\n")
    print("*" * 60)
    print("          CODEALPHA - SECURE CODING REVIEW")
    print("                 SECURITY TEST REPORT")
    print("*" * 60)

    unittest.main(verbosity=2)




