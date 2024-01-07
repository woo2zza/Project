import "./App.css";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import Home from "./pages/Home.js";
import Edit from "./pages/Edit.js";
import New from "./pages/New.js";
import Diary from "./pages/Diary.js";

// conponent
import MyButton from "./components/MyBotton";
import MyHeader from "./components/MyHeader";

function App() {
  return (
    <BrowserRouter>
      <div className="App">
        <MyHeader
          headText={"App"}
          leftChild={
            <MyButton text={"왼쪽버튼"} onClick={() => alert("왼쪽클릭")} />
          }
          rightChild={
            <MyButton text={"오른쪽버튼"} onClick={() => alert("오른쪽버튼")} />
          }
        />
        <h2>App.js</h2>

        <MyButton
          text={"버튼"}
          type={"negative"}
          onClick={() => alert("버튼클릭")}
        />
        <MyButton
          text={"버튼"}
          type={"positive"}
          onClick={() => alert("버튼클릭")}
        />
        <MyButton text={"버튼"} onClick={() => alert("버튼클릭")} />

        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="edit/" element={<Edit />} />
          <Route path="new/" element={<New />} />
          <Route path="diary/:id" element={<Diary />} />
        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;
