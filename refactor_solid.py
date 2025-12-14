
# =====================================================
# Praktikum PBO – Refactoring SOLID
# Studi Kasus: Sistem Validasi Registrasi Mahasiswa
# =====================================================

# ====================
# BEFORE REFACTORING
# (Melanggar SRP, OCP, DIP)
# ====================

class ValidatorManager:
    def validate(self, student):
        if student["sks"] < 20:
            print("Validasi SKS gagal")
            return False

        if not student["has_prerequisite"]:
            print("Validasi prasyarat gagal")
            return False

        print("Registrasi mahasiswa valid")
        return True


# ====================
# AFTER REFACTORING
# (Menerapkan SRP, OCP, DIP)
# ====================

from abc import ABC, abstractmethod

# ===== Abstract Contract (DIP) =====
class Validator(ABC):
    @abstractmethod
    def validate(self, student):
        pass


# ===== SRP: Validator terpisah =====
class SKSValidator(Validator):
    def validate(self, student):
        if student["sks"] < 20:
            print("Validasi SKS gagal")
            return False
        return True


class PrerequisiteValidator(Validator):
    def validate(self, student):
        if not student["has_prerequisite"]:
            print("Validasi prasyarat gagal")
            return False
        return True


# ===== OCP: Validator tambahan tanpa ubah kode lama =====
class IPKValidator(Validator):
    def validate(self, student):
        if student.get("ipk", 0) < 3.0:
            print("Validasi IPK gagal")
            return False
        return True


# ===== High Level Module =====
class RegistrationValidator:
    def __init__(self, validators):
        self.validators = validators  # Dependency Injection

    def validate(self, student):
        for validator in self.validators:
            if not validator.validate(student):
                return False
        print("Registrasi mahasiswa valid")
        return True


# ====================
# PROGRAM UTAMA
# ====================
if __name__ == "__main__":
    student = {
        "sks": 22,
        "has_prerequisite": True,
        "ipk": 3.5
    }

    validators = [
        SKSValidator(),
        PrerequisiteValidator(),
        IPKValidator()
    ]

    registration = RegistrationValidator(validators)
    registration.validate(student)
