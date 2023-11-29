import PropTypes from "prop-types"

function Food({ name }) {
  return <h1>I like {name}</h1>

}

Food.propTypes = {
  name: PropTypes.object.isRequired
}

const foodlist = [
  { name: 'kimchi' },
  { name: 'bibimbap' },
  { name: 'chicken' },
  { name: 'pizza' },
  { name: 'kimbap' },
  { name: 'noodle' },
]

function renderFood(dish){
  return <Food 
      key={dish.name}
      name={dish.name} />
}
function App() {
  return (
    <div>
      {foodlist.map(renderFood)}
    </div>
  );
}
export default App;


