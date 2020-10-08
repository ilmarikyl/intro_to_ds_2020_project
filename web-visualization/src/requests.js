import axios from "axios";

export const getUserInfo = async () => {
  console.log("token", !!process.env.REACT_APP_TOKEN);
  const config = {
    headers: {
      Authorization: `bearer ${process.env.REACT_APP_TOKEN}`,
    },
  };

  const response = await axios.get(
    `https://cors-anywhere.herokuapp.com/https://api.twitter.com/2/users/by?usernames=realdonaldtrump,joebiden&user.fields=description,profile_image_url`,
    config
  );
  return response.data;
};
