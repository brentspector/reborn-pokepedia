import { mount } from "@vue/test-utils";
import Details from "@/views/Details.vue";

describe("Details.vue", () => {
  it("renders details view", () => {
    const mockRoute = {
      params: {
        id: "Outbox",
      },
    };
    const wrapper = mount(Details, {
      global: {
        mocks: {
          $route: mockRoute,
        },
      },
    });
    expect(wrapper.text()).toMatch("Select a Pokemon");
  });
});
