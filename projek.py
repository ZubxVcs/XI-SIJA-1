from datetime import datetime, timedelta

class Habit:
    def __init__(self, name, description=""):
        self.name = name
        self.description = description
        self.history = []

    def add_record(self, date):
        """Tandai kebiasaan ini dilakukan pada tanggal tertentu."""
        self.history.append(date)

class HabitTracker:
    def __init__(self):
        self.habits = {}

    def add_habit(self, habit):
        """Tambahkan kebiasaan baru ke dalam tracker."""
        self.habits[habit.name] = habit

    def mark_habit_done(self, habit_name, date=None):
        """Tandai kebiasaan selesai dilakukan pada tanggal tertentu."""
        if date is None:
            date = datetime.now().date()
        if habit_name in self.habits:
            self.habits[habit_name].add_record(date)
            print(f"Kebiasaan '{habit_name}' telah ditandai selesai pada {date}.")
        else:
            print(f"Kebiasaan '{habit_name}' tidak ditemukan!")
    
    def remove_habit(self, habit_name):
        if habit_name in self.habits:
            del self.habits[habit_name]
            print(f"kebisaan '{habit_name}'telah dihapus")
        else:
             print(f"kebisaan '{habit_name}'tidak ditemukan")


    def weekly_report(self):
        """Buat laporan Harian untuk setiap kebiasaan."""
        report = {}
        today = datetime.now().date()
        one_week_ago = today - timedelta(days=7)
        
        for habit_name, habit in self.habits.items():
            completed_dates = [date for date in habit.history if date >= one_week_ago]
            report[habit_name] = len(completed_dates)
        
        return report

    def show_weekly_report(self):
        report = self.weekly_report()
        print("\nLaporan Kebiasan Harian:")
        for habit_name, count in report.items():
            print(f"{habit_name}: {count} kali dalam sehari terakhir")
        print()

def main():
    tracker = HabitTracker()

    while True:
        print("\n=== Aplikasi Manajemen Kebiasaan ===")
        print("1. Tambah Kebiasaan Baru")
        print("2. Tandai Kebiasaan Selesai")
        print("3. Lihat Laporan Harian")
        print("4. Hapus Kebisaan")
        print("5. Keluar")

        choice = input("Pilih opsi (1-5): ")

        if choice == "1":
            name = input("Nama kebiasaan: ")
            description = input("Deskripsi kebiasaan: ")
            habit = Habit(name, description)
            tracker.add_habit(habit)
            print(f"Kebiasaan '{name}' telah ditambahkan.")

        elif choice == "2":
            habit_name = input("Nama kebiasaan yang ingin ditandai: ")
            tracker.mark_habit_done(habit_name)

        elif choice == "3":
            tracker.show_weekly_report()

        elif choice =="4":
            habit_name =input("nama kebisaan yang ingin dihapus:")
            tracker.remove_habit(habit_name)

        elif choice == "5":
            print("Keluar dari aplikasi.")
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
