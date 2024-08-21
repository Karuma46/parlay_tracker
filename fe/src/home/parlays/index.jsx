import { useEffect, useState } from "react";
import api from "../../services/api";
import { faPlus } from "@fortawesome/free-solid-svg-icons";
import Icon from "../../components/icons";
import ParlayForm from "./parlayForm";

const ParlayCard = ({ parlay }) => {
  return (
    <>
      <div className="card bg-base-100 w-72  overflow-hidden cursor-pointer border border-slate-700 hover:shadow-xl hover:border-slate-600">
        <div className="w-full aspect-[2/1] bg-red-400"></div>
        <div className="card-body p-4">
          <h2 className="card-title text-lg">{parlay.name}</h2>
          <p>{parlay.description}</p>
        </div>
      </div>
    </>
  );
};
const Parlays = () => {
  const [parlays, setParlays] = useState([]);
  const [showParlayForm, setShowParlayForm] = useState(false);

  const getParlays = () => {
    api.parlays.get().then((res) => {
      setParlays(res.data);
    });
  };

  useEffect(() => {
    getParlays();
  }, []);

  return (
    <>
      <div className="w-screen py-8 px-8">
        <p className="text-2xl font-light">Parlays</p>
        <div className="w-full flex py-4">
          {parlays.map((parlay) => (
            <div key={parlay.id}>
              <ParlayCard parlay={parlay} />
            </div>
          ))}
        </div>
      </div>

      <div className="absolute bottom-8 right-8">
        <button className="btn btn-circle btn-outline" onClick={() => setShowParlayForm(true)}>
          <Icon icon={faPlus} size="lg" />
        </button>
      </div>

      <ParlayForm
        visible={showParlayForm}
        hide={() => setShowParlayForm(false)}
      />
    </>
  );
};

export default Parlays;
