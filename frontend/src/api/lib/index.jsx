import {
  createCustomAxios,
  createDefaultAxios,
  createFapiAxios,
} from "./createCustomAxios";

const memberCustomInstance = () => {
  const instance = createCustomAxios("/member");

  return instance;
};

const memberDefaultInstance = () => {
  const instance = createDefaultAxios("/member");

  return instance;
};

const boardCustomInstance = () => {
  const instance = createCustomAxios(`/board`);

  return instance;
};

const boardDefaultInstance = (params) => {
  const instance = createDefaultAxios(
    `/board?page=${params.page ? params.page : 0}&size=${
      params.size ? params.size : 10
    }&sort=${params.sort ? params.sort : "createDateTime,DESC"}&${
      params.type ? params.type : ""
    }`,
  );

  return instance;
};

const boardDetailDefaultInstance = () => {
  const instance = createDefaultAxios(`/board`);

  return instance;
};

const imageDefaultInstance = () => {
  const instance = createDefaultAxios(`/image`);

  return instance;
};

const searchDefaultInstance = () => {
  const instance = createDefaultAxios(`/search`);

  return instance;
};

const commentDefaultInstance = (params) => {
  const instance = createDefaultAxios(
    `/comment?${params.boardId ? params.boardId : ""}&page=${params.page ? params.page : 0}&size=${
      params.size ? params.size : 10
    }&sort=${params.sort ? params.sort : "createDateTime,DESC"}&${
      params.type ? params.type : ""
    }`,
  );

  return instance;
};

const commentCustomInstance = () => {
  const instance = createCustomAxios(`/comment`);

  return instance;
};

const quotationCustomInstance = () => {
  const instance = createCustomAxios(`/quotation`);

  return instance;
};

const quotationCustomListInstance = (params) => {
  const instance = createCustomAxios(
    `/quotation?page=${params.page ? params.page : 0}&size=${
      params.size ? params.size : 10
    }`,
  );
  return instance;
};

const fapiSearchInstance = () => {
  const instance = createFapiAxios(`/search`);

  return instance;
};

const fapiSearchCategoryInstance = () => {
  const instance = createFapiAxios(`/search/program`);

  return instance;
};

const fapiRecommendInstance = () => {
  const instance = createFapiAxios(`/recommend`);

  return instance;
};

const fapiRecommendsInstance = () => {
  const instance = createFapiAxios(`/recommends`);

  return instance;
};

const fapiPartInstance = () => {
  const instance = createFapiAxios(`/parts`);

  return instance;
};

export {
  memberCustomInstance,
  memberDefaultInstance,
  boardCustomInstance,
  boardDefaultInstance,
  boardDetailDefaultInstance,
  searchDefaultInstance,
  imageDefaultInstance,
  commentDefaultInstance,
  commentCustomInstance,
  quotationCustomInstance,
  quotationCustomListInstance,
  fapiSearchInstance,
  fapiSearchCategoryInstance,
  fapiRecommendInstance,
  fapiRecommendsInstance,
  fapiPartInstance,
};
