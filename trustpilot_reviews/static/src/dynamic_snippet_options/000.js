/** @odoo-module **/

import {groupBy} from "@web/core/utils/arrays";
import publicWidget from "@web/legacy/js/public/public_widget";
import DynamicSnippet from "@website/snippets/s_dynamic_snippet/000";
import DynamicSnippetCarousel from "@website/snippets/s_dynamic_snippet_carousel/000";
import {markup} from "@odoo/owl";
import {rpc} from "@web/core/network/rpc";
import OwlMixin from "@trustpilot_reviews/js/mixins"
// import productOptions from './product_options'

const DynamicSnippets = DynamicSnippet.extend({
    // While the selector has 'upcoming_snippet' in its name, it now has a filter
    // option to include ongoing events. The name is kept for backward compatibility.
    selector: ".s_dynamic_snippet",
    disabledInEditableMode: false,

    init: function () {
        this._super.apply(this, arguments);
    },
    _getSearchDomain: function () {
        let searchDomain = this._super.apply(this, arguments);
        return searchDomain;
    },
    async _fetchData() {
        if (this._isConfigComplete()) {
            const nodeData = this.el.dataset;
            const filterFragments = await rpc(
                '/website/snippet/filters',
                Object.assign({
                    'filter_id': parseInt(nodeData.filterId),
                    'template_key': nodeData.templateKey,
                    'limit': parseInt(nodeData.numberOfRecords),
                    'search_domain': this._getSearchDomain(),
                    'with_sample': this.editableMode,
                    'product_context': productOptions(this.el.dataset.name, this.$el),
                }, this._getRpcParameters())
            );
            this.data = filterFragments.map(markup);
        } else {
            this.data = [];
        }
    }
});

const DynamicSnippetsCarousel = DynamicSnippetCarousel.extend({
    // While the selector has 'upcoming_snippet' in its name, it now has a filter
    // option to include ongoing events. The name is kept for backward compatibility.
    selector: "._dynamic_snippet_ratings",
    disabledInEditableMode: false,

    init: function () {
        this._super.apply(this, arguments);
    },
    _getSearchDomain: function () {
        let searchDomain = this._super.apply(this, arguments);
        let filterByTagIds = null
        let snippetName = this.$el.get(0).dataset.name
        if (snippetName) {
            filterByTagIds = this.$el.get(0).dataset.ratingsIds;
        }
        if (filterByTagIds) {
            let groupedByTags = groupBy(
                JSON.parse(filterByTagIds),
                "id"
            );
            for (const tag in groupedByTags) {
                searchDomain = searchDomain.concat([
                    ["id", "in", groupedByTags[tag].map((e) => e.id)],
                ]);
            }
        }
        const allIds = searchDomain
            .filter(([field, operator]) => field === "id" && operator === "in")
            .flatMap(([, , ids]) => ids);
        const mergedIds = [...new Set(allIds)];
        searchDomain =
            searchDomain.length > 0 ? [["id", "in", mergedIds]] : [];
        return searchDomain;
    },
    async _fetchData() {
        if (this._isConfigComplete()) {
            const nodeData = this.el.dataset;
            const filterFragments = await rpc(
                '/website/snippet/filters',
                Object.assign({
                    'filter_id': parseInt(nodeData.filterId),
                    'template_key': nodeData.templateKey,
                    'limit': parseInt(nodeData.numberOfRecords),
                    'search_domain': this._getSearchDomain(),
                    'with_sample': this.editableMode,
                    // 'product_context': productOptions(this.el.dataset.name, this.$el),
                }, this._getRpcParameters())
            );
            this.data = filterFragments.map(markup);
        } else {
            this.data = [];
        }
    },
    _renderContent: function () {
        this._super.apply(this, arguments);
        let dynamic_owl_carousel = $(".dynamic-owl-carousel")
        if (!dynamic_owl_carousel.length) return
        let $items = $(this.$el);
        let itemsLarge = $items.attr("data-number-of-elements") || 4;
        let itemsSmall = $items.attr("data-number-of-elements-small-devices") || 1;
        let carouselInterval = parseInt($items.attr("data-carousel-interval")) || 5000;
        let loop = $items.attr("data-loop") === 'true';
        let dots = $items.attr("data-dots") === 'true';
        let nav = $items.attr("data-nav") === 'true';
        let navText = ["<i class='far fa-chevron-left'></i>", "<i class='far fa-chevron-right'></i>"]
        let autoPlay = $items.attr("data-autoPlay") === 'true';
        let rewind = $items.attr("data-rewind") === 'true';
        let responsive = {
            0: {items: itemsSmall},
            576: {items: itemsSmall},
            768: {items: itemsLarge},
            1200: {items: itemsLarge},
        };
        dynamic_owl_carousel.each(function (index) {
            OwlMixin.initOwlCarousel(
                ".dynamic-owl-carousel",
                15,
                responsive,
                loop,
                1,
                dots,
                nav,
                navText,
                carouselInterval,
                true,
                true,
                true,
                false,
                autoPlay,
                rewind
            );
        });
    }
});

publicWidget.registry.dynamic_snippetsl = DynamicSnippets;
publicWidget.registry.dynamic_snippets_carousel = DynamicSnippetsCarousel;
