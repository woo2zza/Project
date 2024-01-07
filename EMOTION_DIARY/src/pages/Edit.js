import { useNavigate, useSearchParams } from "react-router-dom";
const Home = () => {
  const [serachParams, setserachParams] = useSearchParams();

  const id = serachParams.get("id");
  console.log(id);

  const mode = serachParams.get("mode");
  console.log(mode);

  const navigate = useNavigate();

  return (
    <div>
      <h1>Edit</h1>
      <p>이곳은 일기 수정페이지</p>
      <button onClick={() => setserachParams({ who: "wooseok" })}>
        QS 바꾸기
      </button>
      <button onClick={() => navigate("/")}>Home으로 가기</button>
      <button
        onClick={() => {
          navigate(-1);
        }}
      >
        뒤로가기
      </button>
    </div>
  );
};

export default Home;
