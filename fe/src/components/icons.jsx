import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";

const Icon = ({ icon, size, className }) => {
  return (
    <FontAwesomeIcon
      icon={icon}
      size={size || "sm"}
      fw="bold"
      className={className}
    />
  );
};

export default Icon;
