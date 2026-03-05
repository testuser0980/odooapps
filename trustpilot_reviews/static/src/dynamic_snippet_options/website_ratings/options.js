/** @odoo-module **/

import options from "@web_editor/js/editor/snippets.options";
import s_dynamic_snippet_carousel_options from "@website/snippets/s_dynamic_snippet_carousel/options";
import wUtils from "@website/js/utils";

const dynamicSnippetRatingsOptions = s_dynamic_snippet_carousel_options.extend({
    init: function () {
        this._super.apply(this, arguments);
        this.ratings = {};
        this.modelNameFilter = "trustpilot.reviews";
    },
    _computeWidgetVisibility(widgetName, params) {
        return this._super(...arguments);
    },
    _fetchRatings: function () {
        return this.orm.searchRead("trustpilot.reviews", wUtils.websiteDomain(this), [
            "id",
            "author_name",
        ]);
    },
    _renderCustomXML: async function (uiFragment) {
        await this._super.apply(this, arguments);
        await this._renderRatingSelector(uiFragment);
    },
    _renderRatingSelector: async function (uiFragment) {
        const productCategories = await this._fetchRatings();
        for (let index in productCategories) {
            this.ratings[productCategories[index].id] = productCategories[index];
        }
        const ratingsSelectorEl = uiFragment.querySelector(
            '[data-name="rating_opt"]'
        );
        return this._renderSelectUserValueWidgetButtons(
            ratingsSelectorEl,
            this.ratings
        );
    },
    _setOptionsDefaultValues: function () {
        //   this._setOptionValue("pageId", "all");
        this._setOptionValue('dots', true);
        this._setOptionValue('nav', true);
        this._setOptionValue('autoPlay', true);
        this._super.apply(this, arguments);
    },
});

options.registry.dynamic_snippet_ratings = dynamicSnippetRatingsOptions;

export default dynamicSnippetRatingsOptions;
