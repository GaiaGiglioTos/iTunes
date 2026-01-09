import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleCreaGrafo(self, e):
        self._model._grafo.clear()
        self._model._idMap.clear()

        dTxt = self._view._txtInDurata.value
        if dTxt == "":
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(
                ft.Text("Attenzione, valore minimo di durata non inserito.", color="red"))
            self._view.update_page()
            return
        try:
            d = int(dTxt)
        except ValueError:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(
                ft.Text("Attenzione, valore inserito non valido.", color="red"))
            self._view.update_page()
            return

        self._model.build_graph(d)
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text(f"Grafo creato con {self._model.getNumNodi()} nodi e {self._model.getNumArchi()} archi"))
        self.fillddAlbum()
        self._view.update_page()

    def getSelectedAlbum(self, e):
        pass

    def handleAnalisiComp(self, e):
        if self._view._ddAlbum.value is None:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text("Attenzione, album non selezionato.",
                                                          color="red"))
            self._view.update_page()
            return
        n = self._model._idMap[int(self._view._ddAlbum.value)]
        dim, durata = self._model.getInfoConnessa(n)
        self._view.txt_result.controls.append(ft.Text(f"Componente connessa - {n.Title}"))
        self._view.txt_result.controls.append(ft.Text(f"Dimensione componente = {dim}"))
        self._view.txt_result.controls.append(ft.Text(f"Durata componente = {durata}"))
        self._view.update_page()

    def handleGetSetAlbum(self, e):
        pass

    def fillddAlbum(self):
        self._view._ddAlbum.options.clear()
        album = self._model._grafo.nodes
        for a in album:
            self._view._ddAlbum.options.append(ft.dropdown.Option(text=f"{a.Title}", key = a.AlbumId))

        self._view.update_page()