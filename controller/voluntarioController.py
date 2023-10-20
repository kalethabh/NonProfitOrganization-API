class voluntarioController():
    def add():
        with open(self.file, 'r+', encoding='utf-8') as f:
            data = json.load(f)
            data.append(new_student.__str__())
            f.seek(0)
            json.dump(data, f)
        f.close()
        return new_student